import React, {useState} from 'react';
import { Form, Input, Button } from 'antd';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { UserOutlined, MailOutlined, LockOutlined } from '@ant-design/icons';
import * as actions from '../store/actions/auth';

const FormItem = Form.Item;



function RegistrationForm(props) {
  const [confirmDirty, setConfirmDirty] = useState(false) 

  const handleSubmit = (e) => {
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err, values) => {
      if (!err) {
        this.props.onAuth(
            values.userName,
            values.email,
            values.password,
            values.confirm
        );
        this.props.history.push('/');
      }
    });
  }

  const handleConfirmBlur = (e) => {
    const value = e.target.value;
    setConfirmDirty(confirmDirty || !!value );
  }

  const compareToFirstPassword = (rule, value, callback) => {
    const form = props.form;
    if (value && value !== form.getFieldValue('password')) {
      callback('Two passwords that you enter is inconsistent!');
    } else {
      callback();
    }
  }

  const validateToNextPassword = (rule, value, callback) => {
    const form = props.form;
    if (value && confirmDirty) {
      form.validateFields(['confirm'], { force: true });
    }
    callback();
  }

  return (
    <Form onSubmit={handleSubmit}>
      
      <Form.Item
          name="userName"
              rules = {[{ required: true, message: 'Please input your username!' }]}>
              <Input prefix={<UserOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} placeholder="Username" />
      </Form.Item>
      
      <Form.Item rules={[{
            type: 'email', message: 'The input is not valid E-mail!',
          }, {
            required: true, message: 'Please input your E-mail!',
          }]}>
          <Input prefix={<MailOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} placeholder="Email" />
      </Form.Item>

      <FormItem rules={[{
            required: true, message: 'Please input your password!',
          }, {
            validator: validateToNextPassword,
          }]}>
          <Input prefix={<LockOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} type="password" placeholder="Password" />
      </FormItem>

      <FormItem rules={[{
            required: true, message: 'Please confirm your password!',
          }, {
            validator: compareToFirstPassword,
          }]}>
          <Input prefix={<LockOutlined style={{ color: 'rgba(0,0,0,.25)' }} />} type="password" placeholder="Password" onBlur={handleConfirmBlur} />
      </FormItem>

      <FormItem>
      <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
          Signup
      </Button>
      Or 
      <NavLink 
          style={{marginRight: '10px'}} 
          to='/login/'> login
      </NavLink>
      </FormItem>

    </Form>
  );
}

const WrappedRegistrationForm = Form.create()(RegistrationForm);

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, email, password1, password2) => dispatch(actions.authSignup(username, email, password1, password2)) 
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(WrappedRegistrationForm);
