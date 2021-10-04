import React, {useState, useEffect} from "react";
import axios from "axios";
import { connect } from "react-redux";
import { Button, Card } from "antd";
import ArticleForm from "../components/Form";
import {host} from "../store/utility";

function ArticleDetail(props) {
  const [article, setArticle] = useState({})

  const articleID = props.match.params.articleID;

  useEffect(() => {
    axios.get(host + `api/${articleID}`).then(res => {
      setArticle(res.data);
    });
  }, [articleID])

  const handleDelete = event => {
    event.preventDefault();
    const articleID = props.match.params.articleID;
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${props.token}`
    };
    axios.delete(host + `api/${articleID}/delete/`)
    .then(res => {
      if (res.status === 204) {
        props.history.push(`/`);
      }
    })
  };

  return (
    <div>
      <Card title={article.title}>
        <p> {article.content} </p>
      </Card>
      <ArticleForm
        {...props}
        token={props.token}
        requestType="put"
        articleID={props.match.params.articleID}
        btnText="Update"
      />
      <form onSubmit={handleDelete}>
        <Button type="danger" htmlType="submit">
          Delete
        </Button>
      </form>
    </div>
  );
}

const mapStateToProps = state => {
  return {
    token: state.token
  };
};

export default connect(mapStateToProps)(ArticleDetail);
