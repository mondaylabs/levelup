import axios from "axios";
import {COURSES} from "./urls.js";

export const loadData = (url, setState) => {
    axios.get(url)
        .then(res => setState(res.data))
        .catch(err => console.error(err))
}