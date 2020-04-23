import * as React from 'react';
import {
  Chart,
  BarSeries,
  Title,
  ArgumentAxis,
  ValueAxis,
} from '@devexpress/dx-react-chart-material-ui';
import { Animation } from '@devexpress/dx-react-chart';
import Paper from '@material-ui/core/Paper';
import ListItem from '@material-ui/core/ListItem';

const data = [
  { year: '1950', population: 2.525 },
  { year: '1960', population: 3.018 },
  { year: '1970', population: 3.682 },
  { year: '1980', population: 4.440 },
  { year: '1990', population: 5.310 },
  { year: '2000', population: 6.127 },
  { year: '2010', population: 6.930 },
];

export default class SemiMaster extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      offsetParent: {
        offsetLeft: 0,
        offsetTop: 0,
      },
      data,
      redmine: []
    };
  }

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/defect');
      const redmine = await res.json();
      this.setState({
        redmine
      });
    } catch (e) {
      console.log(e);
    }
  }

  masters=[];
  masterCnt=[];
  
  render() {
    return (
      <div>
        <Chart
          data={this.state.redmine}
          height='250'
        >
          <ArgumentAxis />
          <ValueAxis max={7} />

          <BarSeries
            valueField="num"
            argumentField="master"
          />
          <Title text="결함 수정중인 담당자 현황" />
          <Animation />
        </Chart>
        <Paper>
          {this.state.redmine.map(item => (
            <ListItem>
              <div key={item.num}>
                <div>{item.num}</div>
                <div>{item.state}</div>
                <div>{item.author}</div>
                <div>{item.master}</div>
                <div>{item.title}</div>
                <div>{item.start}</div>
              </div>
            </ListItem>
          ))}
        </Paper>
      </div>
    );
  }
}