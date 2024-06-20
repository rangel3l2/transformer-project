import { AnalysisService } from './../services/analysis.service';
import { AnalysisData } from './../models/AnalysisData';
import { Component, OnInit } from '@angular/core';
import { DisplayInfoAnalysisComponent } from './display-info-analysis/display-info-analysis.component';
import { DurvalTriangleComponent } from './durval-triangle/durval-triangle.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DatePipe } from '@angular/common';

const limits = {
  hidrogen: { normal: 150, alert: 300, alarm: 700 },
  methane: { normal: 40, alert: 100, alarm: 200 },
  acetylene: { normal: 1, alert: 3, alarm: 50 },
  ethylene: { normal: 50, alert: 100, alarm: 200 },
  ethane: { normal: 65, alert: 100, alarm: 150 },
  carbon_monoxide: { normal: 350, alert: 570, alarm: 1000 },
  carbon_dioxide: { normal: 2500, alert: 4000, alarm: 10000 },
};
@Component({
  selector: 'analysis',
  standalone: true,
  imports: [DisplayInfoAnalysisComponent, DurvalTriangleComponent],
  templateUrl: './analysis.component.html',
  styleUrl: './analysis.component.scss',
  providers: [DatePipe],
})
export class AnalysisComponent implements OnInit {
  analysisData?: AnalysisData[];

  constructor(private analysisService: AnalysisService, private datePipe: DatePipe) {}
  ngOnInit(): void {
    this.getAnalysis();
  }
  classifyStatus(data: AnalysisData[]) {
    const dataFixed = data.forEach((item) => {
      const hidrogenLevels = item.chemical.hidrogen;
      const methaneLevels = item.chemical.methane;
      const acetyleneLevels = item.chemical.acetylene;
      const ethyleneLevels = item.chemical.ethylene;
      const ethaneLevels = item.chemical.ethane;
      const carbonMonoxideLevels = item.chemical.carbon_monoxide;
      const carbonDioxideLevels = item.chemical.carbon_dioxide;

      if (
        hidrogenLevels > limits.hidrogen.alarm ||
        methaneLevels > limits.methane.alarm ||
        acetyleneLevels > limits.acetylene.alarm ||
        ethyleneLevels > limits.ethylene.alarm ||
        ethaneLevels > limits.ethane.alarm ||
        carbonMonoxideLevels > limits.carbon_monoxide.alarm ||
        carbonDioxideLevels > limits.carbon_dioxide.alarm
      ) {
        item.analysis.status = 'Alarm';
      } else if (
        hidrogenLevels > limits.hidrogen.alert ||
        methaneLevels > limits.methane.alert ||
        acetyleneLevels > limits.acetylene.alert ||
        ethyleneLevels > limits.ethylene.alert ||
        ethaneLevels > limits.ethane.alert ||
        carbonMonoxideLevels > limits.carbon_monoxide.alert ||
        carbonDioxideLevels > limits.carbon_dioxide.alert
      ) {
        item.analysis.status = 'Alert';
      } else {
        item.analysis.status = 'Normal';
      }
    });

    return dataFixed;
  }
  getAnalysis() {
    this.analysisService.getAnalysis().subscribe({
      next: (data : AnalysisData[]) => {
        console.log('Analysis Data:', data);
        data.forEach((item) => {
          const dataFixed = this.datePipe.transform(item.analysis.sampling_date, 'dd MMMM yyyy', 'pt-BR');

          item.analysis.sampling_date = dataFixed;
        }
        );
        this.classifyStatus(data);
        this.analysisData = data;
      },
      error: (error) => {
        console.error('Analysis Error:', error);
      },
    });
  }
}
