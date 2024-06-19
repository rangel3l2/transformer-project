import { Component, Input } from '@angular/core';
import { AnalysisData } from '../../models/AnalysisData';

@Component({
  selector: 'durval-triangle',
  standalone: true,
  imports: [],
  templateUrl: './durval-triangle.component.html',
  styleUrl: './durval-triangle.component.scss'
})
export class DurvalTriangleComponent {
@Input() analysisData?: AnalysisData[];
}
