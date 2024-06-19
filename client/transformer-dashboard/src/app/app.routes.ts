import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { TransformerComponent } from './transformer/transformer.component';
import { AnalysisComponent } from './analysis/analysis.component';
import { ReportComponent } from './report/report.component';
export const routes: Routes = [
  {
    path: '',
    component: DashboardComponent,
  },
  {
    path: 'dashboard',
    component: DashboardComponent,
  },

  {
    path: 'transformers',
    component: TransformerComponent,
  },
  {
    path: 'transformers/:id',
    component: TransformerComponent,
  },
  {
    path: 'analysis',
    component: AnalysisComponent,
  },
  {
    path: 'report',
    component: ReportComponent,
  },
  {
    path: '**',
    component: PageNotFoundComponent,
  },
];
