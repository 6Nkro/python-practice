import { configureStore } from "@reduxjs/toolkit";
import commonSlice from "./slices/commonSlice";
import modalSlice from "./slices/modalSlice";
export const store = configureStore({
  reducer: {
    common: commonSlice,
    modal: modalSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
