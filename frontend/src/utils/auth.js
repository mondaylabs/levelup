import axios from "axios";
import {SIGN_IN, SIGN_UP} from "./urls.js";
export const user = JSON.parse(localStorage.getItem('user'))


export const register = (email, password, first_name, last_name) => {
    return axios.post(SIGN_UP, {
        email, password, first_name, last_name
    })

}
export const login = (email, password) => {
    return axios.post(SIGN_IN, {
        email, password
    })
}

