import { CommonState } from "../types/state";

export const saveCommonStateToLocal = (state: CommonState) => {
  try {
    localStorage.setItem("commonState", JSON.stringify(state));
  } catch (error) {
    console.error("Error saving commonState to local storage:", error);
  }
};

export const loadCommonStateFromLocal = (): CommonState | undefined => {
  try {
    const commonState = localStorage.getItem("commonState");
    return commonState ? JSON.parse(commonState) : undefined;
  } catch (error) {
    console.error("Error loading commonState from local storage:", error);
    return undefined;
  }
};
