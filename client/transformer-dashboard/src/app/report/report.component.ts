import { AnalysisData } from './../models/AnalysisData';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { jsPDF } from 'jspdf';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';
import { AnalysisService } from '../services/analysis.service';
import { DatePipe } from '@angular/common';

const limits = {
  hidrogen: { normal: 150, alert: 300, alarm: 700 },
  methane: { normal: 40, alert: 100, alarm: 200 },
  acetylene: { normal: 1, alert: 3, alarm: 50 },
  ethylene: { normal: 50, alert: 100, alarm: 200 },
  ethane: { normal: 65, alert: 100, alarm: 150 },
  carbon_monoxide: { normal: 350, alert: 570, alarm: 1000 },
  carbon_dioxide: { normal: 2500, alert: 4000, alarm: 10000 }
};

@Component({
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.scss'],
  imports: [RouterModule],
  providers: [DatePipe],
  standalone: true
})
export class ReportComponent implements OnInit {
   
  analysisData : AnalysisData[] = [];
  
  constructor(private analysisService: AnalysisService, private datePipe: DatePipe) {}
  ngOnInit(): void {
    this.getAnalysisData() 
  }
  getAnalysisData() {
    this.analysisService.getAnalysis()  
      .subscribe({
        next: (data) => {
          console.log('Analysis Data:', data);
          this.analysisData = data;
          this.classifyStatus();
        },
        error: (error) => {
          console.error('Analysis Error:', error);
        }
      });
  }
  classifyStatus() {
    if(this.analysisData.length === 0) return;
    this.analysisData.forEach(item => {
      const hidrogenLevels = item.chemical.hidrogen;
      const methaneLevels = item.chemical.methane;
      const acetyleneLevels = item.chemical.acetylene;
      const ethyleneLevels = item.chemical.ethylene;
      const ethaneLevels = item.chemical.ethane;
      const carbonMonoxideLevels = item.chemical.carbon_monoxide;
      const carbonDioxideLevels = item.chemical.carbon_dioxide;
      if(hidrogenLevels > limits.hidrogen.alarm || methaneLevels > limits.methane.alarm || acetyleneLevels > limits.acetylene.alarm || ethyleneLevels > limits.ethylene.alarm || ethaneLevels > limits.ethane.alarm || carbonMonoxideLevels > limits.carbon_monoxide.alarm || carbonDioxideLevels > limits.carbon_dioxide.alarm) {
        item.analysis.status = 'Alarm';
      } else if(hidrogenLevels > limits.hidrogen.alert || methaneLevels > limits.methane.alert || acetyleneLevels > limits.acetylene.alert || ethyleneLevels > limits.ethylene.alert || ethaneLevels > limits.ethane.alert || carbonMonoxideLevels > limits.carbon_monoxide.alert || carbonDioxideLevels > limits.carbon_dioxide.alert) {
        item.analysis.status = 'Alert';
      } else {
        item.analysis.status = 'Normal';
      }
    }
    );
    
  }
  
  exportPDF() {
    let doc = new jsPDF();
    let y = 10;

    this.analysisData.forEach(item => {

      doc.text(`Analysis ID: ${item.analysis.id_analisys}`, 10, y);
      y += 10;
      doc.text(`Status: ${item.analysis.status}`,10 , y);

      y += 10;
      const dataFixed = this.datePipe.transform(item.analysis.sampling_date, 'dd MMMM yyyy');

      doc.text(`Data Analisys:${dataFixed}`, 10, y);
      y += 10;
      // Add more fields as necessary
    });

    doc.save('report.pdf');
  }

  exportExcel() {
    const worksheet = XLSX.utils.json_to_sheet(this.analysisData);
    const workbook = { Sheets: { 'data': worksheet }, SheetNames: ['data'] };
    const excelBuffer: any = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
    this.saveAsExcelFile(excelBuffer, 'report');
  }
              
  private saveAsExcelFile(buffer: any, fileName: string): void {
    const data: Blob = new Blob([buffer], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8'
    });
    saveAs(data, `${fileName}.xlsx`);
  }
}
