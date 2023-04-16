import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../../store/store";
import {
  closeLoginModal,
  closeSignUpModal,
} from "../../store/slices/modalSlice";
import { TextFieldProps, ButtonProps } from "@mui/material";
import FormModal from "../../components/commons/CustomModals";

const LoginFormModal = () => {
  const isOpen = useSelector((state: RootState) => state.modal.loginModal);
  const dispatch = useDispatch();

  const textFieldData: TextFieldProps[] = [
    { label: "이메일", type: "email", autoFocus: true },
    { label: "비밀번호", type: "password" },
  ];

  const buttonData: ButtonProps[] = [
    {
      onClick: () => dispatch(closeLoginModal()),
      children: "로그인",
    },
    {
      onClick: () => dispatch(closeSignUpModal()),
      children: "회원가입",
    },
  ];

  return (
    <FormModal
      isOpen={isOpen}
      onClose={() => dispatch(closeLoginModal())}
      title={<div>로그인</div>}
      textFieldData={textFieldData}
      buttonData={buttonData}
    />
  );
};

const SignUpFormModal = () => {
  const isOpen = useSelector((state: RootState) => state.modal.signUpModal);
  const dispatch = useDispatch();

  const textFieldData: TextFieldProps[] = [
    { label: "이메일", type: "email", autoFocus: true },
    { label: "닉네임", type: "text" },
    { label: "비밀번호", type: "password" },
    { label: "비밀번호 확인", type: "password" },
  ];

  const buttonData: ButtonProps[] = [
    {
      onClick: () => dispatch(closeSignUpModal()),
      children: "등록",
    },
  ];

  return (
    <FormModal
      isOpen={isOpen}
      onClose={() => dispatch(closeSignUpModal())}
      title={<div>회원가입</div>}
      textFieldData={textFieldData}
      buttonData={buttonData}
    />
  );
};

export { LoginFormModal, SignUpFormModal };
