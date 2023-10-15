import React from 'react';
import axios from "axios";
import {QUESTIONS} from "../utils/urls.js";
import {useNavigate} from "react-router-dom";

const CardCurse = ({showCourse, courses}) => {

    const navigate = useNavigate()
    const passTest = (id) => {
        axios.get(QUESTIONS.replace('id', id))
            .then(res => navigate(`/question/${res.data.results[0].id}/${id}`))
            .catch(err => console.error(err))
    }

    if (courses) return (
        <div className="flex my-[48px] justify-around">
            <div className="w-[50%] flex gap-[20px] flex-col justify-between">
                <div className="mt-[48px]">
                    <h1 className='mb-[48px] font-bold text-[38px] leading-[112%] text-[#44ad4e] origin-top-left rotate-[-2deg]'>{courses.results[showCourse].name}</h1>
                    {/*<ul className='mt-[20px]'>*/}
                    {/*    {courses.results[showCourse].topics.map(topic => (*/}
                    {/*         <li*/}
                    {/*             key={topic.id}*/}
                    {/*             className='mt-[16px] text-[18px] leading-[135%] flex items-start gap-[21px] text-center before:content-[""] before:w-[8px] before:h-[8px] before:rounded-lg before:mt-[0.4em] before:bg-[#44ad4e]'>*/}
                    {/*             {topic.name}*/}
                    {/*    </li>*/}

                    {/*    ))}*/}
                    {/*</ul>*/}
                    <p>{courses.results[showCourse].description}</p>
                </div>
                <button
                    className="btn-wide btn btn-active  text-white bg-[#44ad4e]"
                    onClick={() => passTest(courses.results[showCourse].id)}
                >Pass text</button>
            </div>
            <div className="w-[40%]">
                <img className='object-cover'
                     src="https://camo.githubusercontent.com/0fd2667849df9f18b863a2fc9fdf275d28c0e69bae657009213dbbba08295d02/68747470733a2f2f7261772e6769746875622e636f6d2f436972636c6543492d5075626c69632f63696d672d707974686f6e2f6d61737465722f696d672f636972636c652d707974686f6e2e7376673f73616e6974697a653d74727565"
                     alt=""

                />
            </div>
        </div>
    )
    else return  'loading'
};

export default CardCurse;
