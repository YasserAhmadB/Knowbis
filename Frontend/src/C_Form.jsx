import Axios from 'axios';
import {useState} from 'react'
import './c_form.css';

const C_Form = () => {

    const url = "http://192.168.1.2:8000/platform/categories/";
    // const url = "https://reqres.in/api/users";
    const [data, setData] = useState({
        title: "",
        brief: "",  
        smg: ""
    });

    function handle(e){
        const newdata =  {...data};
        newdata[e.target.id] = e.target.value;
        setData(newdata);
        console.log(newdata);

    }

    function submit(e){
        e.preventDefault();
        console.log(data);
        console.log(url)
        Axios.post(url,{
            // name: data.title,
            // job: data.brief
            title:"muneer"
            // brief: data.brief,
            // smg: data.smg,
        })
        .then(res=>{
            console.log(res.data);
        })
        

    }


    return (
        <div className="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
              <div className="wrapper wrapper--w680">
                <div className="card card-4">
                  <div className="card-body">
                    <h2 className="title">Create Course</h2>
                    <form onSubmit={(e) => submit(e)}>
                      <div className="row row-space">
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Title</label>
                            <input
                              className="input--style-4"
                              type="text"
                              onChange= {(e) => handle(e)}
                              id="title" value={data.title}
                            />
                          </div>
                        </div>
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Brief</label>
                            <input
                              className="input--style-4"
                              type="text"
                              onChange= {(e) => handle(e)}
                              id="brief" value={data.brief}
                            />
                          </div>
                        </div>
                      </div>
                      <div className="row row-space">
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Something</label>
                            <div className="input-group-icon">
                              <input
                                className="input--style-4 js-datepicker"
                                type="text"
                                name="birthday"
                                onChange= {(e) => handle(e)}
                                id="smg" value={data.smg}
                              />
                              <i
                                className="zmdi zmdi-calendar-note input-icon js-btn-calendar"
                              ></i>
                            </div>
                          </div>
                        </div>
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Type</label>
                            <div className="p-t-10">
                              <label className="radio-container m-r-45"
                                >Videos
                                <input 
                                type="radio" 
                                // checked="checked" 
                                onChange= {(e) => handle(e)}
                                />
                                <span className="checkmark"></span>
                              </label>
                              <label className="radio-container"
                                >Documents
                                <input type="radio" />
                                <span className="checkmark"></span>
                              </label>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className="row row-space">
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Something</label>
                            <input 
                            className="input--style-4" 
                            type="text" 
                            onChange= {(e) => handle(e)}
                            id="smg" value={data.smg}
                            />
                          </div>
                        </div>
                        <div className="col-2">
                          <div className="input-group">
                            <label className="label">Something</label>
                            <input 
                            className="input--style-4" 
                            type="text" 
                            onChange= {(e) => handle(e)}
                            id="smg" value={data.smg}
                            />
                          </div>
                        </div>
                      </div>
                      <div className="input-group">
                        <label className="label">Category</label>
                        <div className="rs-select2 js-select-simple select--no-search">
                          <select className="input--style-4" >
                            <option disabled="disabled" selected="selected">
                              Choose option
                            </option>
                            <option>C 1</option>
                            <option>C 2</option>
                            <option>C 3</option>
                          </select>
                          <div className="select-dropdown"></div>
                        </div>
                      </div>
                      <div className="p-t-15">
                        <button className="btn btn--radius-2 btn--blue" type="submit">
                          Submit
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
        </div>
  )
}

export default C_Form;