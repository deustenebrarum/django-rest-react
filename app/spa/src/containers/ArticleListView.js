import React, {useState, useEffect} from "react";
import axios from "axios";
import Articles from "../components/Article";
import ArticleForm from "../components/Form";
import {host} from "../store/utility";

function ArticleList(props) {
  const [articles, setArticles] = useState([])

  const fetchArticles = () => {
    axios.get(host + "api/").then(res => {
      setArticles(res.data)
    });
  }

  useEffect(() => {
    fetchArticles();
  }, [])

  useEffect(() => {
    fetchArticles();
  }, [props.token])
  
  return (
    <div>
      <Articles data={articles} /> <br />
      <h2> Create an article </h2>
      <ArticleForm requestType="post" articleID={null} btnText="Create" />
    </div>
  );
}

export default ArticleList;
