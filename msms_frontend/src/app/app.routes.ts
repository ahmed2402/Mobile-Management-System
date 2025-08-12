import { Routes } from '@angular/router';
// Update the import path and extension to match the actual file location and name
import { Sales } from './pages/sales/sales';

export const routes: Routes = [
  { path: '', redirectTo: 'sales', pathMatch: 'full' },
  { path: 'sales', component: Sales },
];