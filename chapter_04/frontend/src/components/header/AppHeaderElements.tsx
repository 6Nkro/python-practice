import React, { MouseEventHandler, ReactElement } from "react";
import {
  Theme,
  styled,
  AppBar,
  IconButton,
  Typography,
  Button,
  IconButtonProps,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";

export const HeaderAppBar = styled(AppBar)(({ theme }: { theme: Theme }) => ({
  zIndex: theme.zIndex.drawer + 1,
  color: theme.palette.mode === "dark" ? undefined : "grey",
  backgroundColor: theme.palette.mode === "dark" ? undefined : "white",
}));

export const Hamburger: React.FC<IconButtonProps> = ({ onClick }) => (
  <IconButton
    children={<MenuIcon />}
    edge="start"
    sx={{ mr: 2 }}
    onClick={onClick}
  />
);

interface AppTitleProps {
  text: string;
  icon: ReactElement;
  onClick: MouseEventHandler<HTMLElement>;
}

export const AppTitle: React.FC<AppTitleProps> = ({ text, icon, onClick }) => (
  <Button
    startIcon={icon}
    variant="text"
    size="small"
    sx={{ textTransform: "none" }}
    onClick={onClick}
  >
    <TitleText variant="h6">{text}</TitleText>
  </Button>
);

const TitleText = styled(Typography)(({ theme }: { theme: Theme }) => ({
  color: theme.palette.mode === "dark" ? "white" : "black",
  fontWeight: 600,
}));
