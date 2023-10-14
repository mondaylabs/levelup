import React, {useEffect, useState} from 'react';
import Button from "../components/common/Button.jsx";
import {useNavigate, useParams} from "react-router-dom";

const tests = {
    count: 4,
    results: [
        {
            id: 1,
            text: "First Question?",
            answers: [
                {
                    id: 1,
                    text: "Answer 1"
                },
                {
                    id: 2,
                    text: "Answer 2"
                },
                {
                    id: 3,
                    text: "Answer 3"
                }
            ]
        },
        {
            id: 2,
            text: "Python Question 1?",
            answers: [
                {
                    id: 4,
                    text: "Answer 2.1"
                },
                {
                    id: 5,
                    text: "Answer 2.2"
                },
                {
                    id: 6,
                    text: "Answer 2.3"
                }
            ]
        },
        {
            id: 3,
            text: "Python Question 2?",
            answers: [
                {
                    id: 7,
                    text: "Answer 3.1"
                },
                {
                    id: 8,
                    text: "Answer 3.2"
                },
                {
                    id: 9,
                    text: "Answer 3.3"
                }
            ],
        }, {
            id: 4,
            text: "Python Question 3?",
            answers: [
                {
                    id: 10,
                    text: "Answer 4.1"
                },
                {
                    id: 11,
                    text: "Answer 4.2"
                },
                {
                    id: 12,
                    text: "Answer 4.3"
                }
            ],
        },

    ]
}


function QuestionDetail({}) {
    const navigate = useNavigate()
    const letters = ['A', 'B', 'C', 'D']
    const [thisQuestion, setThisQuestion] = useState(null)
    const [passed, setPassed] = useState([])
    const params = useParams()

    useEffect(() => {
        setThisQuestion(tests.results.find(i => i.id === +params.id))
    }, [params])


    return (
        <div className="flex">
            <div className="w-[20%] bg-gray-50  h-[100vh] shadow-xl
             flex gap-[24px] items-center p-[15px] py-[10px] flex-col rounded-se-[100px]">
                <div className="flex items-center justify-center pt-[32px]">
                    <div className="radial-progress text-success" style={{"--value": 100, "--size": "150px"}}>100%</div>
                </div>
                <ul className="steps steps-vertical max-h-[70vh] overflow-auto w-[90%] text-center ">
                    {tests.results.length ? tests.results.map(question => (
                        <li
                            onClick={() => navigate(`/question/${question.id}`)}
                            className={`${params.id == question.id ? 'bg-gray-100' : ''} step step-success  cursor-pointer rounded-xl  hover:bg-gray-100 `}
                            key={question.id}>
                            Question {question.id}
                        </li>

                    )) : ''}

                </ul>
            </div>
            <div className="flex flex-col p-[40px] gap-10 w-[100%] justify-between">
                <div className="flex flex-col p-[40px] gap-10 w-[100%]">
                    <div className="flex flex-col gap-3 w-[100%]">
                        {thisQuestion ? <>
                                <h1 className="text-3xl font-bold">{thisQuestion.text}</h1>
                                <br/>
                                <div className="flex flex-col gap-3 ">
                                    {thisQuestion.answers.map((answer, index) => (
                                        <label className="flex items-center gap-3" key={answer.id}>
                                            <input type="radio" className="radio radio-success" name="answer"/>
                                            <span className="text-xl">{letters[index]}: {answer.text}</span>
                                        </label>

                                    ))}
                                </div>

                            </>
                            : ''}

                    </div>
                    <div className="flex items-center gap-3 justify-center w-[100%]">
                        <Button
                            text={'Prev'}
                            className={'btn-success text-white w-[20%]'}
                        />
                        <Button
                            text={'Next'}
                            className={'btn btn-success text-white w-[20%]'}
                        />
                    </div>
                </div>
                <div className="card w-[100%] bg-orange-50 shadow-xl">
                    <div className="card-body">
                        <div className="card-actions justify-end">
                            <button className="btn btn-square hover:bg-red-300 btn-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none"
                                     viewBox="0 0 24 24"
                                     stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                          d="M6 18L18 6M6 6l12 12"/>
                                </svg>
                            </button>
                        </div>
                        <p>We are using cookies for no reason.</p>
                    </div>
                </div>
            </div>
        </div>

    );
}

export default QuestionDetail;