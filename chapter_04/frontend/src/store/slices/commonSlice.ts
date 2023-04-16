import { createSlice } from "@reduxjs/toolkit";
import {
  loadCommonStateFromLocal,
  saveCommonStateToLocal,
} from "../localStorage";
import { CommonState } from "../../types/state";

const initialState: CommonState = loadCommonStateFromLocal() || {
  nightMode: false,
  sideBar: true,
};

const commonSlice = createSlice({
  name: "common",
  initialState,
  reducers: {
    toggleNightMode: state => {
      state.nightMode = !state.nightMode;
      saveCommonStateToLocal(state);
    },
    toggleSideBar: state => {
      state.sideBar = !state.sideBar;
      saveCommonStateToLocal(state);
    },
  },
});

export const { toggleNightMode, toggleSideBar } = commonSlice.actions;
export default commonSlice.reducer;
