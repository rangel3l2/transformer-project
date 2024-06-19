import { DisplayDataComponent } from './display-data/display-data.component';
import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { MenuButtonComponent } from './menu-button/menu-button.component';
import { LineChartComponent } from './line-chart/line-chart.component';
import { EquipmentService } from '../services/equipment.service';
import { RouterModule } from '@angular/router';

type data = {
  title: string;
};


@Component({
  selector: 'dashboard',
  standalone: true,
  imports: [
    DisplayDataComponent,
    MenuButtonComponent,
    LineChartComponent,
    RouterModule
   

  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent implements OnInit {
 
 data: data = {title: "Visão Geral"};
 equipmentData: any;
constructor(private equipmentService: EquipmentService) { }
  ngOnInit(): void {    
    this.getEquipment();
  }
  getEquipment() {
    this.equipmentService.getEquipment()
      .subscribe({
        next: (data) => { // Handle successful response
          console.log('Equipment Data:', data);
          this.equipmentData = data; // Assign data to the component property
        },
        error: (error) => { // Handle errors
          console.error('Equipment Error:', error);
        }
      });
  }
}
