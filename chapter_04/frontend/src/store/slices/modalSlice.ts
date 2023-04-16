import { createSlice } from "@reduxjs/toolkit";
import { ModalState } from "../../types/state";

const initialState: ModalState = {
  loginModal: false,
  signUpModal: false,
};

const modalSlice = createSlice({
  name: "modal",
  initialState,
  reducers: {
    openLoginModal: state => {
      state.loginModal = true;
    },
    closeLoginModal: state => {
      state.loginModal = false;
    },
    openSignUpModal: state => {
      state.signUpModal = true;
    },
    closeSignUpModal: state => {
      state.signUpModal = false;
    },
  },
});

export const {
  openLoginModal,
  closeLoginModal,
  openSignUpModal,
  closeSignUpModal,
} = modalSlice.actions;
export default modalSlice.reducer;
