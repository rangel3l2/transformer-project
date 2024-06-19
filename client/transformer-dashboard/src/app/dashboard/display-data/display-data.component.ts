import { Transformer } from './../../models/Transformer';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'display-data',
  standalone: true,
  imports: [],
  templateUrl: './display-data.component.html',
  styleUrl: './display-data.component.scss'
})
export class DisplayDataComponent implements OnInit {
  @Input() transformer?: Transformer[]; 
  ngOnInit(): void {
      
  }
}
