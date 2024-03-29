import axios from "axios";

interface SignUpData {
  user_name: string;
  user_email: string;
  password: string;
  chk_password: string;
}

export const signUp = async (signUpData: SignUpData) => {
  try {
    const response = await axios.post("/api/account/signup/", signUpData);
    console.log(response);
  } catch (error: any) {
    console.error(error.response.data);
  }
};
