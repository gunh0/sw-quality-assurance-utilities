import React from "react";

import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";

const StepProgress = () => {
    return (
        <div>
            <Progress percent={50} />
            <Progress percent={25} />
            <Progress percent={75} />
            <Progress percent={99} />
            <Progress percent={100} />
        </div>
    );
}

export default StepProgress;