import React from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useTheme } from "@mui/material";
import { AppDispatch, RootState } from "../../store/store";
import { toggleNightMode } from "../../store/slices/commonSlice";
import HomeIcon from "@mui/icons-material/Home";
import LightModeIcon from "@mui/icons-material/LightMode";
import ModeNightIcon from "@mui/icons-material/ModeNight";
import {
  SideBarDrawer,
  SideBarButtonProps,
} from "../../components/sideBar/SideBarElements";

const SideBarContainer = () => {
  const isNightMode = useTheme().palette.mode === "dark";
  const isOpen = useSelector((state: RootState) => state.common.sideBar);

  const navigate = useNavigate();
  const dispatch = useDispatch<AppDispatch>();
  const sideBarButtonData: SideBarButtonProps[] = [
    {
      text: "Home",
      icon: <HomeIcon />,
      onClick: () => navigate("/"),
    },
    {
      text: isNightMode ? "LightMode" : "NightMode",
      icon: isNightMode ? <LightModeIcon /> : <ModeNightIcon />,
      onClick: () => dispatch(toggleNightMode()),
    },
  ];

  return <SideBarDrawer isOpen={isOpen} buttonData={sideBarButtonData} />;
};

export default SideBarContainer;
