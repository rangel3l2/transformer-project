import { CommonModule } from '@angular/common';
import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
//import { Chart, ChartModule} from 'angular-highcharts';
import { HighchartsChartModule } from 'highcharts-angular';
import * as Highcharts from 'highcharts';
@Component({
  selector: 'line-chart',
  standalone: true,
  imports: [CommonModule, HighchartsChartModule],
  templateUrl: './line-chart.component.html',
  styleUrl: './line-chart.component.scss',
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class LineChartComponent {

  
  Highcharts: typeof Highcharts = Highcharts;
  chartOptions: Highcharts.Options = {
    chart: {
      type: 'line',
      backgroundColor: 'white',
      plotBorderColor: '#CCCCCC',
      plotBorderWidth: 1
    },
    title: {
      text: 'Transformadores com defeito'
    },
    xAxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    },
    series: [{
      data: [0, 2, 3, 9, 5, 6, 8],
      type: 'line',
      color: 'red'
    }]
  };
 
}
