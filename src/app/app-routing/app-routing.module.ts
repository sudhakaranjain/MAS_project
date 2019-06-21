import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from '../dashboard/dashboard.component';
import {AnalysisComponent} from '../analysis/analysis.component';
import {SolutionComponent} from '../solution/solution.component';
import {DemoComponent} from '../demo/demo.component';

const routes: Routes = [
  {
    path: 'home',
    component: DashboardComponent,
  },
  {
    path: 'analysis',
    component: AnalysisComponent,
  },
  {
    path: 'solution',
    component: SolutionComponent
  },
  {
    path: 'demo',
    component: DemoComponent
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule { }
