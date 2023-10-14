import React, {useEffect, useState} from 'react';
import Navbar from "../components/Navbar.jsx";
import CardCurse from "../components/CardCurse";
import {getCourses} from "../utils/promises.js";

function Home() {
    const [courses, setCourses] = useState([])

    useEffect(() => {
        getCourses()
    }, [])
    return (
        <div>
            <Navbar/>
            <div className="container mx-auto flex-col">
                <div className="mt-[24px] mb-[48px]">
                    <h1 className='font-bold text-[38px] mx-auto text-center w-[535px] mb-[48px]'>Преподаватели, с
                        которыми тебе будет интересно</h1>
                    <div className="flex gap-[12px] flex-wrap">
                        <button className="btn btn-success text-white">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                        <button className="btn">Button</button>
                    </div>
                </div>
                <div className='mx-auto my-[24px] w-[90%] h-[2px] bg-[#44ad4e]'>

                </div>
                <CardCurse/>
            </div>
        </div>

    );
}

export default Home;