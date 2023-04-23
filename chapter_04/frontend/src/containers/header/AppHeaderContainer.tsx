import React from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { AppDispatch } from "../../store/store";
import { toggleSideBar } from "../../store/slices/commonSlice";
import { Box, Button } from "@mui/material";
import BookIcon from "@mui/icons-material/Book";
import {
  AppTitle,
  Hamburger,
  HeaderAppBar,
} from "../../components/header/AppHeaderElements";
import { openLoginModal, openSignUpModal } from "../../store/slices/modalSlice";
import { LoginFormModal, SignUpFormModal } from "./FormModalContainer";

export const AppHeaderContainer = () => {
  const dispatch = useDispatch<AppDispatch>();
  const navigate = useNavigate();

  return (
    <>
      <HeaderAppBar position="fixed">
        <Box
          sx={{
            display: "flex",
            height: 64,
            alignItems: "center",
            justifyContent: "space-between",
          }}
        >
          <Box sx={{ flexGrow: 1, whiteSpace: "nowrap", pl: 3 }}>
            <Hamburger onClick={() => dispatch(toggleSideBar())} />
            <AppTitle
              text="Chapter_04"
              icon={<BookIcon color="info" />}
              onClick={() => navigate("/")}
            />
          </Box>
          <Box sx={{ pr: 3 }}>
            <Button
              onClick={() => dispatch(openLoginModal())}
              children="로그인"
            />
            <Button
              onClick={() => dispatch(openSignUpModal())}
              children="회원가입"
            />
          </Box>
        </Box>
      </HeaderAppBar>
      <LoginFormModal />
      <SignUpFormModal />
    </>
  );
};

export default AppHeaderContainer;
