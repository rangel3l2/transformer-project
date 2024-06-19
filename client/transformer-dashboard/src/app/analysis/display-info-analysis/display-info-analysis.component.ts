import { AnalysisData } from './../../models/AnalysisData';
import { Component, ElementRef, HostListener, Input, OnInit, ViewChild } from '@angular/core';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'display-info-analysis',
  standalone: true,
  imports: [],
  templateUrl: './display-info-analysis.component.html',
  styleUrls: ['./display-info-analysis.component.scss'],
  providers: [DatePipe],
})
export class DisplayInfoAnalysisComponent implements OnInit {
  @ViewChild('canvas', { static: true }) canvasRef!: ElementRef<HTMLCanvasElement>;
  @Input() analysisData?: AnalysisData[];
  currentIndex: number = 0;
  constructor(private datePipe: DatePipe) {}
   ngOnInit(): void {
    this.fixDate();
    this.drawTriangle();
  }
  nextItem() {
    if (this.analysisData) {
      this.currentIndex = (this.currentIndex + 1) % this.analysisData.length;
      this.fixDate();
    }
  }

  previousItem() {
    this.fixDate()
    if (this.analysisData) {
      this.currentIndex = (this.currentIndex - 1 + this.analysisData.length) % this.analysisData.length; // Handle negative index
    }
  }

 

  fixDate() {
    if (this.analysisData) {
      const dataFixed = this.datePipe.transform(this.analysisData[this.currentIndex].analysis.sampling_date, 'dd MMMM yyyy');
     this.analysisData[this.currentIndex].analysis.sampling_date = dataFixed;
    }
  }

  @HostListener('window:resize')
  onResize() {
    this.drawTriangle();
  }

  drawTriangle() {
    if (this.canvasRef) {
      const canvas = this.canvasRef.nativeElement;
      const context = canvas.getContext('2d');
      if (context) {
        // Redimensiona o canvas para corresponder ao tamanho do contêiner
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
      
        // Limpa o canvas
        context.clearRect(0, 0, canvas.width, canvas.height);

        // Desenha o triângulo
        const vertexTopX = canvas.width / 2;
        const vertexTopY = canvas.height * 0.1;
        const vertexLeftX = canvas.width * 0.1;
        const vertexLeftY = canvas.height * 0.9;
        const vertexRightX = canvas.width * 0.9;
        const vertexRightY = canvas.height * 0.9;

        context.beginPath();
        context.moveTo(vertexTopX, vertexTopY); // Vértice superior
        context.lineTo(vertexLeftX, vertexLeftY); // Vértice inferior esquerdo
        context.lineTo(vertexRightX, vertexRightY); // Vértice inferior direito
        context.closePath();
        context.lineWidth = 1.2;
        context.stroke();

        const drawPoint = (x: number, y: number) => {
          context.beginPath();
          context.arc(x, y, 3, 0, 2 * Math.PI); // Desenha um ponto com raio 3
          context.fillStyle = '#FF0000'; // Cor dos pontos
          context.fill();
          context.closePath();
        };

        // Função para dividir um segmento em n partes e desenhar os pontos
        const divideSegment = (
          x1: number,
          y1: number,
          x2: number,
          y2: number,
          n: number
        ) => {
          for (let i = 1; i < n; i++) {
            const x = x1 + (x2 - x1) * (i / n);
            const y = y1 + (y2 - y1) * (i / n);
            drawPoint(x, y);
          }
        };

        // Dividir os lados do triângulo em 10 partes e desenhar os pontos
        const divisions = 10;
        divideSegment(vertexTopX, vertexTopY, vertexLeftX, vertexLeftY, divisions); // Lado esquerdo
        divideSegment(vertexLeftX, vertexLeftY, vertexRightX, vertexRightY, divisions); // Base
        divideSegment(vertexRightX, vertexRightY, vertexTopX, vertexTopY, divisions); // Lado direito

        // Desenha a linha paralela à lateral esquerda do triângulo
        const offset = 50; // Defina o quanto a linha estará afastada da lateral esquerda do triângulo
        const lineStartX = canvas.width / 6;
        const lineStartY = canvas.height - 5;
        const lineEndX = vertexTopX + offset;
        const lineEndY = vertexTopY;

        context.beginPath();
        context.moveTo(lineStartX, lineStartY); // Começa no ponto paralelo à base do triângulo
        context.lineTo(lineEndX, lineEndY); // Linha paralela à lateral esquerda do triângulo
        context.strokeStyle = '#006600'; // Cor da linha
        context.stroke();
        context.closePath();

        // Desenha a linha paralela ao lado superior do triângulo
        const offsetTop = 50; // Defina o quanto a linha estará afastada do lado superior do triângulo
        const lineTopStartX = vertexLeftX;
        const lineTopStartY = vertexLeftY - offsetTop * ((vertexLeftY - vertexTopY) / (vertexRightX - vertexLeftX)) * 2.5;
        const lineTopEndX = vertexRightX;
        const lineTopEndY = vertexRightY - offsetTop * ((vertexRightY - vertexTopY) / (vertexRightX - vertexLeftX)) * 2.5;

        context.beginPath();
        context.moveTo(lineTopStartX, lineTopStartY); // Começa no ponto paralelo ao lado superior do triângulo
        context.lineTo(lineTopEndX, lineTopEndY); // Linha paralela ao lado superior do triângulo
        context.stroke();
        context.closePath();

        // Linha paralela à lateral direita do triângulo
        const lineRightStartX = vertexRightX / 2 + 10; // Ponto inicial X da linha
        const lineRightStartY = vertexRightY; // Ponto inicial Y da linha
        const lineRightEndX = vertexLeftX; // Ponto final X da linha (mesmo que a linha paralela à lateral esquerda)
        const lineRightEndY = lineEndY; // Ponto final Y da linha (mesmo que a linha paralela à lateral esquerda)

        context.beginPath();
        context.moveTo(lineRightStartX, lineRightStartY + offset - 10); // Começa no ponto paralelo à base do triângulo
        context.lineTo(lineRightEndX, lineRightEndY / 2); // Linha paralela à lateral direita do triângulo
        context.stroke();
        context.closePath();

        // Desenha linhas adicionais e texto no triângulo (continuação de seu código)

        context.beginPath();
        context.moveTo(vertexLeftX + 110, vertexLeftY); // Vértice superior
        context.lineTo(vertexLeftX + 220, vertexLeftY - 160); // Vértice inferior esquerdo
        context.strokeStyle = '#000000';
        context.lineWidth = 2;
        context.stroke();
        context.closePath();

        context.beginPath();
        context.moveTo(vertexLeftX * 4 + 20, lineEndY + 46);
        context.lineTo(vertexRightX / 2 + 55, vertexRightY / 1.8);
        context.lineTo(vertexRightX / 2 + 30, vertexRightY / 1.5);
        context.lineTo(vertexRightX - 125, vertexRightY);
        context.stroke();
        context.closePath();

        context.beginPath();
        context.moveTo(vertexLeftX * 4 + 36, lineEndY + 23);
        context.lineTo(vertexRightX / 2 + 95, vertexRightY / 1.8);
        context.stroke();
        context.closePath();

        context.beginPath();
        context.moveTo(vertexRightX / 2 + 114, vertexRightY / 2);
        context.lineTo(vertexRightX / 1.5, vertexRightY / 1.55);
        context.lineTo(vertexRightX / 1.2, vertexRightY);
        context.stroke();
        context.closePath();

        context.beginPath();
        context.moveTo(vertexTopX + 43, vertexTopY + 60);
        context.lineTo(vertexTopX + 25, vertexTopY * 3.3);
        context.stroke();

        // Adiciona texto ao canvas
        context.font = '12px Arial';
        context.fillStyle = '#000000';
        context.fillText('PD', 240, 25);
        context.fillText('T1', 245, 65);
        context.fillText('T2', 290, 125);
        context.fillText('T3', 350, 270);
        context.fillText('DT', 300, 270);
        context.fillText('D2', 230, 270);
        context.fillText('D1', 190, 220);
        context.fillText('CH4 %', 70, 185);
        context.fillText('C2H4 %', 375, 180);
        context.fillText('C2H2 %', 100, 350);

        context.fillStyle = ' #0000FF';
        context.fillText('0', 260, 40);
        context.fillText('10', 280, 70);
        context.fillText('20', 300, 100);
        context.fillText('30', 315, 125);
        context.fillText('40', 335, 150);
        context.fillText('50', 355, 175);
        context.fillText('60', 375, 205);
        context.fillText('70', 395, 235);
        context.fillText('80', 415, 260);
        context.fillText('90', 435, 285);
        context.fillText('100', 455, 315);
        context.fillText('100', 220, 40);
        context.fillText('90', 205, 70);
        context.fillText('80', 185, 100);
        context.fillText('70', 165, 125);
        context.fillText('60', 145, 150);
        context.fillText('50', 125, 175);
        context.fillText('40', 105, 205);
        context.fillText('30', 85, 235);
        context.fillText('20', 65, 260);
        context.fillText('10', 45, 285);
        context.fillText('0', 30, 315);
        context.fillText('0', 445, 340);
        context.fillText('10', 405, 340);
        context.fillText('20', 365, 340);
        context.fillText('30', 325, 340);
        context.fillText('40', 285, 340);
        context.fillText('50', 245, 340);
        context.fillText('60', 205, 340);
        context.fillText('70', 165, 340);
        context.fillText('80', 125, 340);
        context.fillText('90', 85, 340);
        context.fillText('100', 45, 340);
      }
    }
  }
}
