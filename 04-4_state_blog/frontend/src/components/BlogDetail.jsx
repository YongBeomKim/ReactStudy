import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const BlogDetail = (props) => {
		
		const [blog, setBlog] = useState({});
		
    useEffect(() => {
			const slug = props.match.params.id;
			const urlink = `${process.env.REACT_APP_API_URL}/api/blog/${slug}`
			const fetchData = async() => {
				try{
					const res = await axios.get(urlink);
					setBlog(res.data);
				}
				catch (error) {
					console.log(error);
				}
			}
			fetchData(); // run init
    }, [props.match.params.id]);

		// https://ko.reactjs.org/docs/dom-elements.html
    const createBlog = () => {
        return {__html: blog.content}
    };
    
		const capitalizeFirstLetter = (word) => {
			if (word)
				return word.charAt(0).toUpperCase() + word.slice(1);
			return '';
		};
    
    return(
			<div className="container mt-3">
				<h1 className='display-2'>{blog.title}</h1>
				<h2 className='text-muted mt-3'>Category: {capitalizeFirstLetter(blog.category)}</h2>
					<h4>{blog.month} {blog.day}</h4>
				<div className="mt-5 mb-5" dangerouslySetInnerHTML={createBlog()} />
				<hr /> 
				<p className='lead mb-5'>
					<Link to="/blog" className="font-weight-bold">
						Back to Blog
					</Link>
				</p>
			</div>
    );
};

export default BlogDetail;