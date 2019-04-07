import { string } from "prop-types";
import { bgColor } from "./Cell";

export const CELLS_FETCH = () => ({
    type: 'CELLS_FETCH',
});
export const DATA_RECEIVED = () => ({
    type: 'DATA_RECEIVED',
});
export const UPDATE_VALUE = (payload: any) => ({
    type: 'UPDATE_VALUE', payload
    }
);