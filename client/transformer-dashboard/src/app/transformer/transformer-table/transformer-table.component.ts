import { Component, Input, OnInit } from '@angular/core';
import {CdkTableModule} from '@angular/cdk/table';
import { Transformer } from '../../models/Transformer';


@Component({
  selector: 'transformer-table',
  standalone: true,
  imports: [CdkTableModule],
  templateUrl: './transformer-table.component.html',
  styleUrl: './transformer-table.component.scss'
})
export class TransformerTableComponent implements OnInit {
  @Input() transformerData!: any
  displayedColumns: string[] = ['tag', 'serie_id', 'place_installed'];
 
  constructor() { }

  ngOnInit(): void {

  }

}
