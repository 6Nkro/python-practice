import React, { MouseEventHandler } from "react";
import { Drawer } from "@mui/material";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

interface SidebarDrawerProps {
  isOpen: boolean;
  buttonData: SideBarButtonProps[];
}

export const SideBarDrawer: React.FC<SidebarDrawerProps> = ({
  isOpen,
  buttonData,
}) => (
  <Drawer variant="permanent" sx={setDrawerStyles(isOpen)}>
    {buttonData.map((buttonProps, index) => (
      <SideBarButton key={index} {...buttonProps} />
    ))}
  </Drawer>
);

const setDrawerStyles = (isOpen: boolean) => ({
  width: isOpen ? 240 : 60,
  flexShrink: 0,
  "& .MuiDrawer-paper": {
    width: isOpen ? 240 : 60,
    boxSizing: "border-box",
    pt: 10,
  },
});

export interface SideBarButtonProps {
  text: string;
  icon: React.ReactElement;
  onClick: MouseEventHandler<HTMLElement>;
}

export const SideBarButton: React.FC<SideBarButtonProps> = ({
  text,
  icon,
  onClick,
}) => (
  <div style={{ overflowX: "hidden" }}>
    <ListItemButton key={text} onClick={onClick}>
      <ListItemIcon>{icon}</ListItemIcon>
      <ListItemText primary={text} />
    </ListItemButton>
  </div>
);
