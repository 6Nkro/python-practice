import React, { ReactElement } from "react";
import { TextFieldProps } from "@mui/material/TextField/TextField";
import { ButtonProps } from "@mui/material/Button/Button";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from "@mui/material";

interface FormModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: ReactElement;
  textFieldData: TextFieldProps[];
  buttonData: ButtonProps[];
}

export const FormModal: React.FC<FormModalProps> = ({
  isOpen,
  onClose,
  title,
  textFieldData,
  buttonData,
}) => {
  return (
    <Dialog
      open={isOpen}
      onClose={onClose}
      PaperProps={{ style: { width: "100%", maxWidth: "500px" } }}
    >
      <DialogTitle>{title}</DialogTitle>
      <form>
        <DialogContent>
          {textFieldData.map((textFieldProps, index) => (
            <TextField
              key={index}
              margin="dense"
              autoComplete="off"
              fullWidth
              {...textFieldProps}
            />
          ))}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          {buttonData.map((buttonProps, index) => (
            <Button key={index} type="button" fullWidth {...buttonProps} />
          ))}
        </DialogActions>
      </form>
    </Dialog>
  );
};

export default FormModal;
