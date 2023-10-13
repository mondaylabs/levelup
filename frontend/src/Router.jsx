import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from "./pages/Home.jsx";
import QuestionDetail from "./pages/QuestionDetail.jsx";

function Router() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/question/:id" element={<QuestionDetail/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default Router;