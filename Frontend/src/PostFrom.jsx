import { Axios } from 'axios';
import {useState} from 'react';

const PostFrom = () => {

    const url = "";
    const [data, setData] = useState({
        name: "",
        date: "",
        iduser: ""
    });

    function handle(e){
        const newdata =  {...data};
        newdata[e.target.id] = e.target.value;
        setData(newdata);
        console.log(newdata);

    }

    function submit(e){
        e.preventDefault();
        Axios.post(url,{
            name: data.name,
            data: data.date,
            iduser: data.iduser,
        })
        .then(res=>{
            console.log(res.data);
        })

    }


    return (
        <div>
            <form onSubmit={(e) => submit(e)}>
            <input onChange= {(e) => handle(e)} id="name" value={data.name} type="text" placeholder="Course Name"></input>
            <input onChange= {(e) => handle(e)} id="date" value={data.date} type="date" placeholder="date"></input>
            <input onChange= {(e) => handle(e)} id="iduser" value={data.iduser} type="number" placeholder="Course ID"></input>
            <button>Submit</button>
            </form>
        </div>
  )
}

export default PostFrom;