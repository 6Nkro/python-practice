import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../../store/store";
import {
  closeLoginModal,
  closeSignUpModal,
  openSignUpModal,
} from "../../store/slices/modalSlice";
import { TextFieldProps, ButtonProps } from "@mui/material";
import FormModal from "../../components/commons/CustomModals";
import { signUp } from "../../services/accountService";

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
      onClick: () => {
        dispatch(closeLoginModal());
        dispatch(openSignUpModal());
      },
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

  const [formData, setFormData] = useState({
    user_email: "",
    user_name: "",
    password: "",
    chk_password: "",
  });
  const handleInputChange = (
    e: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>,
    field: string
  ) => setFormData({ ...formData, [field]: e.target.value });

  const fields = [
    { label: "이메일", type: "email", name: "user_email", autoFocus: true },
    { label: "닉네임", type: "text", name: "user_name" },
    { label: "비밀번호", type: "password", name: "password" },
    { label: "비밀번호 확인", type: "password", name: "chk_password" },
  ];

  const textFieldData: TextFieldProps[] = fields.map(field => ({
    ...field,
    onChange: e => handleInputChange(e, field.name),
  }));

  const buttonData: ButtonProps[] = [
    {
      onClick: () => signUp(formData),
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
