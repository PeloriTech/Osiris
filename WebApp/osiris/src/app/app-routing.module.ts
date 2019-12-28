import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardPageComponent} from './pages/dashboard-page/dashboard-page.component';
import {LoginPageComponent } from './pages/login-page/login-page.component';
import {SettingsPageComponent} from './pages/settings-page/settings-page.component';

import {PipesPageComponent} from './pages/pipes-page/pipes-page.component';
import {CreateNewPipeComponent} from './pages/pipes-page/create-new-pipe/create-new-pipe.component';

import {DatasetManagerPageComponent} from './pages/dataset-manager-page/dataset-manager-page.component';
import {CreateDatasetPageComponent} from './pages/dataset-manager-page/create-dataset-page/create-dataset-page.component';
import {DatasetPageComponent} from './pages/dataset-manager-page/dataset-page/dataset-page.component';

import {MapReportPageComponent} from './pages/report-pages/map-report-page/map-report-page.component';

const routes: Routes = [

    { path: '', component: DashboardPageComponent },
    { path: 'login', component: LoginPageComponent },
    { path: 'dashboard', component: DashboardPageComponent},
    { path: 'settings', component: SettingsPageComponent},

    { path: 'pipes/manager', component: PipesPageComponent },
    { path: 'pipes/launch', component: CreateNewPipeComponent},
    
    { path: 'dataset/manager', component: DatasetManagerPageComponent},
    { path: 'dataset/create', component: CreateDatasetPageComponent},
    { path: 'dataset/view', component: DatasetPageComponent},

    { path: 'report/map', component: MapReportPageComponent},
    { path: '**', redirectTo: '' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
