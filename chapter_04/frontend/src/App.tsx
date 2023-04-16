import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";
import { useSelector } from "react-redux";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { GlobalStyles, CssBaseline, Box } from "@mui/material";
import { SnackbarProvider } from "notistack";
import { RootState } from "./store/store";
import AppHeaderContainer from "./containers/header/AppHeaderContainer";
import SideBarContainer from "./containers/sideBar/SideBarContainer";
import HomeContainer from "./containers/home/HomeContainer";

const App = () => {
  const [queryClient] = useState(() => new QueryClient());
  const nightMode = useSelector((state: RootState) => state.common.nightMode);

  const theme = createTheme({
    palette: {
      mode: nightMode ? "dark" : "light",
    },
  });

  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <SnackbarProvider maxSnack={3}>
          <Box sx={{ display: "flex" }}>
            <GlobalStyles styles={{ body: { overflowY: "scroll" } }} />
            <CssBaseline />
            <Router>
              <AppHeaderContainer />
              <SideBarContainer />
              <Box sx={{ pt: 8, flexGrow: 1 }}>
                <Routes>
                  <Route path="/" element={<HomeContainer />} />
                </Routes>
              </Box>
            </Router>
          </Box>
        </SnackbarProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
};

export default App;
