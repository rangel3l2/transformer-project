
import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { PageHeaderComponent } from './page-header/page-header.component';
import { SideNavComponent } from './side-nav/side-nav.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule ,RouterOutlet, PageHeaderComponent, SideNavComponent, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'transformer-dashboard';
}
