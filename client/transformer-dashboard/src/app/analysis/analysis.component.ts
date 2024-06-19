import { AnalysisService } from './../services/analysis.service';
import { AnalysisData } from './../models/AnalysisData';
import { Component, OnInit } from '@angular/core';
import { DisplayInfoAnalysisComponent } from './display-info-analysis/display-info-analysis.component';
import { DurvalTriangleComponent } from './durval-triangle/durval-triangle.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
@Component({
  selector: 'analysis',
  standalone: true,
  imports: [DisplayInfoAnalysisComponent, DurvalTriangleComponent],
  templateUrl: './analysis.component.html',
  styleUrl: './analysis.component.scss',
})
export class AnalysisComponent implements OnInit {
  analysisData?: AnalysisData[];

  constructor(private analysisService: AnalysisService) {}
  ngOnInit(): void {
    this.getAnalysis();
  }
  getAnalysis() {
    
    this.analysisService.getAnalysis().subscribe({
      next: (data) => {
        console.log('Analysis Data:', data);
        this.analysisData = data;
      },
      error: (error) => {
        console.error('Analysis Error:', error);
      },
    });
  }
}
