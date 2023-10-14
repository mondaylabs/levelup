import axios from "axios";
import {COURSES} from "./urls.js";

export const getCourses = () => {
    axios.get(COURSES)
        .then(res => console.log(res.data))
        .catch(err => console.error(err))
}