import React from 'react';
import MaterialTable from 'material-table';

export default function MainStatusTable() {
  const [state, setState] = React.useState({
    columns: [
      { title: '부문', field: 'part', },
      { title: '버전', field: 'version', },
      { title: '(차수) 적합/부적합', field: 'content', },
      {
        title: '확인항목수',
        field: 'checkCnt',
      },
      {
        title: '결함수', field: 'defectsCnt',
      }
    ],
    data: [
      { part: '기능', version: '2.2.2-2.7.1', content: '(2차) 적합', checkCnt: 300, defectsCnt: 0 },
      { part: '정합성', },
    ],
  });

  return (
    <MaterialTable
      title="품질점검 상태"
      columns={state.columns}
      data={state.data}
      editable={{
        onRowAdd: (newData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              setState((prevState) => {
                const data = [...prevState.data];
                data.push(newData);
                return { ...prevState, data };
              });
            }, 600);
          }),
        onRowUpdate: (newData, oldData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              if (oldData) {
                setState((prevState) => {
                  const data = [...prevState.data];
                  data[data.indexOf(oldData)] = newData;
                  return { ...prevState, data };
                });
              }
            }, 600);
          }),
        onRowDelete: (oldData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              setState((prevState) => {
                const data = [...prevState.data];
                data.splice(data.indexOf(oldData), 1);
                return { ...prevState, data };
              });
            }, 600);
          }),
      }}
    />
  );
}
