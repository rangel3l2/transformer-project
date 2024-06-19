import { Component, OnInit } from '@angular/core';
import { TransformerTableComponent } from './transformer-table/transformer-table.component';
import { EquipmentService } from '../services/equipment.service';

@Component({
  selector: 'transformer',
  standalone: true,
  imports: [TransformerTableComponent],
  templateUrl: './transformer.component.html',
  styleUrl: './transformer.component.scss'
})
export class TransformerComponent implements OnInit {
  equipmentData: any;
  
  ngOnInit(): void {
     this.getEquipment(); 
  }
  constructor(private equipmentService: EquipmentService){

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
