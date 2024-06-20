import { AnalysisData } from './../models/AnalysisData';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { jsPDF } from 'jspdf';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';
import { AnalysisService } from '../services/analysis.service';
import { DatePipe } from '@angular/common';
import autoTable, { RowInput } from 'jspdf-autotable';

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
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.scss'],
  imports: [RouterModule],
  providers: [DatePipe],
  standalone: true,
})
export class ReportComponent implements OnInit {
  analysisData: AnalysisData[] = [];

  constructor(
    private analysisService: AnalysisService,
    private datePipe: DatePipe
  ) {}
  ngOnInit(): void {
    this.getAnalysisData();
  }
  getAnalysisData() {
    this.analysisService.getAnalysis().subscribe({
      next: (data) => {
        console.log('Analysis Data:', data);

        this.classifyStatus(data);
        this.analysisData = data;
      },
      error: (error) => {
        console.error('Analysis Error:', error);
      },
    });
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

  exportPDF() {
    const doc = new jsPDF();

    // Add content to the PDF.
    doc.setFontSize(16);
    doc.text('Relatório de Analise', 10, 10);
    doc.setFontSize(12);
    doc.text('Dados gerais de analise de transformadores de potência.', 10, 20);

    // Create a table using `jspdf-autotable`.

    const headers = [
      [
        'Código',
        'Tag Equipamento',
        'Total Gases',
        'Lugar Instalado',
        'Data Amostra',
        'Resultado',
      ],
    ];

    const bodyData: RowInput[] = this.analysisData.map((item) => {
      // Ensure all cell values are strings (or cast them)
      return [
        String(item.analysis.id_analisys),
        item.equipment.tag || 'N/A',
        item.chemical.total_gases || 'N/A', // Handle potential missing 'totalGases' property
        item.equipment.place_installed || 'N/A',
        this.datePipe.transform(item.analysis.sampling_date, 'dd MMMM yyyy', 'pt-BR') ||
          'N/A',
        item.analysis.status || 'N/A',
      ];
    });

    autoTable(doc, {
      head: headers,
      body: bodyData,
      startY: 30, // Adjust the `startY` position as needed.
    });

    doc.save();
  }

  exportExcel() {
    const headers = [
      [
        'Código',
        'Tag Equipamento',
        'Total Gases',
        'Lugar Instalado',
        'Data Amostra',
        'Resultado',
      ],
    ];
    const bodyData: string[][] = this.analysisData.map((item) => {
      // Ensure all cell values are strings (or cast them)
      return [
        String(item.analysis.id_analisys), // Convert to string
        item.equipment.tag || 'N/A', // Use 'N/A' for missing values
        String(item.chemical?.total_gases) || 'N/A', // Convert or use 'N/A'
        item.equipment.place_installed || 'N/A',
        this.datePipe.transform(item.analysis.sampling_date, 'dd/MM/yyyy', 'pt-BR') || 'N/A',
        String(item.analysis.status) || 'N/A', // Convert to string
      ];
    });

    const worksheet = XLSX.utils.aoa_to_sheet(headers.concat(bodyData)); // Combine headers and body for worksheet
    const workbook = { Sheets: { data: worksheet }, SheetNames: ['data'] };
    const excelBuffer = XLSX.write(workbook, {
      bookType: 'xlsx',
      type: 'array',
    });

    this.saveAsExcelFile(excelBuffer, 'report');
  }

  private saveAsExcelFile(buffer: any, fileName: string): void {
    const data: Blob = new Blob([buffer], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8',
    });
    saveAs(data, `${fileName}.xlsx`);
  }
}
