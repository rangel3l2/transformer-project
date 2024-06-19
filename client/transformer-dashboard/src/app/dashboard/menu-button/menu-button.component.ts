import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router'; // Import Router

@Component({
  selector: 'menu-button',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './menu-button.component.html',
  styleUrl: './menu-button.component.scss'
})
export class MenuButtonComponent {

  constructor(private router: Router) {} // Inject Router

  navigateTo() {
    console.log('Navigating to dashboard');
    this.router.navigate(['/report']);
  }
}
