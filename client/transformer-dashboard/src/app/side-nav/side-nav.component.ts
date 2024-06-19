import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'side-nav',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './side-nav.component.html',
  styleUrl: './side-nav.component.scss'
})
export class SideNavComponent {
items: {icon: string, title:string;link:string}[]= [
  {icon: 'overview', title: 'Visão Geral', link: '/dashboard'},
  {icon: 'construction', title: 'Transformadores', link: '/transformers'},
  {icon: 'experiment', title:'Análises', link: '/analysis'},
];
}
