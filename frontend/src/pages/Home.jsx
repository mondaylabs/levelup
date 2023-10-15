import React, {useEffect, useState} from 'react';
import Navbar from "../components/Navbar.jsx";
import CardCurse from "../components/CardCurse";
import {loadData} from "../utils/promises.js";
import {COURSES, QUESTIONS} from "../utils/urls.js";
import SignUpForm from "../components/SignUpForm";

function Home() {
    const [courses, setCourses] = useState(null)
    const [showCourse, setShowCourse] = useState(0)
    const [questions, setQuestions]= useState([])


    useEffect(() => {
        loadData(COURSES, setCourses)
        loadData(QUESTIONS.replace('id', '10'), setQuestions)
    }, [])

    console.log(questions)
    console.log(courses)
    return (
        <div>
            <Navbar/>
            <div className="container mx-auto flex-col">
                <div className="mt-[24px] mb-[48px]">
                    <h1 className='font-bold text-[38px] mx-auto text-center w-[535px] mb-[48px]'>Курсе, с
                        которыми тебе будет интересно</h1>
                    <div className="flex gap-[12px] flex-wrap">
                        {courses && courses.results.map((course, index) => (
                            <button
                                key={course.id}
                                className={`btn ${index === showCourse ? ' btn-success text-white' : ''}`}
                                onClick={() => setShowCourse(index)}
                            >
                                {course.name}
                            </button>

                        ))}

                    </div>
                </div>
                <div className='mx-auto my-[24px] w-[90%] h-[2px] bg-[#44ad4e]'>
                    <SignUpForm/>
                </div>
                <CardCurse showCourse={showCourse} courses={courses}/>
            </div>
        </div>

    );
}

export default Home;