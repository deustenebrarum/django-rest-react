import React from "react";
import { Form, Input, Button } from "antd";
import { connect } from "react-redux";
import axios from "axios";
import {host} from '../store/utility';

const FormItem = Form.Item;


function ArticleForm(props) {
  
  const handleFormSubmit = async (event, requestType, articleID) => {
    event.preventDefault();

    const postObj = {
      title: event.target.elements.title.value,
      content: event.target.elements.content.value
    }

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${props.token}`,
    };
    
    if (requestType === "post") {
      await axios.post(host + "api/create/", postObj)
        .then(res => {
          if (res.status === 201) {
            props.history.push(`/`);
          }
        })
    } else if (requestType === "put") {
      await axios.put(host + `api/${articleID}/update/`, postObj)
        .then(res => {
          if (res.status === 200) {
            props.history.push(`/`);
          }
        })
    }
  };

  return (
    <div>
      <Form
        onSubmit={event =>
          handleFormSubmit(
            event,
            this.props.requestType,
            this.props.articleID
          )
        }
      >
        <FormItem label="Title">
          <Input name="title" placeholder="Put a title here" />
        </FormItem>
        <FormItem label="Content">
          <Input name="content" placeholder="Enter some content ..." />
        </FormItem>
        <FormItem>
          <Button type="primary" htmlType="submit">
            {props.btnText}
          </Button>
        </FormItem>
      </Form>
    </div>
  );
}

const mapStateToProps = state => {
  return {
    token: state.token
  };
};

export default connect(mapStateToProps)(ArticleForm);
