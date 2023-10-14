import axios from "axios";
import {SIGN_UP} from "./urls.js";

export const register = (email, password, first_name, last_name) => {
   return axios.post(SIGN_UP, {
        email, password, first_name, last_name
    })

}
export const signIn = () => {

}