import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {
  MatListModule,
  MatIconModule,
  MatSidenavModule,
  MatTabsModule,
  MatToolbarModule,
  MatCardModule,
  MatRadioModule,
  MatCheckboxModule,
  MatOptionModule,
  MatSelectModule,
  MatInputModule,
  MatButtonModule,
  MatTableModule,
  MatStepperModule,
  MatGridListModule,
  MatMenuModule,
  MatExpansionModule
} from '@angular/material';

import {MatFormFieldModule} from '@angular/material/form-field';


import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';

import {SideMenuComponent} from './foundation/side-menu/side-menu.component';
import {TopBarComponent} from './foundation/top-bar/top-bar.component';
import {LoginPageComponent} from './pages/login-page/login-page.component';
import { PipesPageComponent } from './pages/pipes-page/pipes-page.component';
import { SettingsPageComponent } from './pages/settings-page/settings-page.component';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { CreateNewPipeComponent } from './pages/pipes-page/create-new-pipe/create-new-pipe.component';
import { DatasetManagerPageComponent } from './pages/dataset-manager-page/dataset-manager-page.component';
import { MapReportPageComponent } from './pages/report-pages/map-report-page/map-report-page.component';
import { CreateDatasetPageComponent } from './pages/dataset-manager-page/create-dataset-page/create-dataset-page.component';
import { DatasetPageComponent } from './pages/dataset-manager-page/dataset-page/dataset-page.component';


@NgModule({
  declarations: [
    AppComponent,
    SideMenuComponent,
    TopBarComponent,
    LoginPageComponent,
    PipesPageComponent,
    SettingsPageComponent,
    DashboardPageComponent,
    CreateNewPipeComponent,
    DatasetManagerPageComponent,
    MapReportPageComponent,
    CreateDatasetPageComponent,
    DatasetPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule,
    MatSidenavModule,
    MatTabsModule,
    MatToolbarModule,
    MatMenuModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule,
    HttpClientModule,
    MatFormFieldModule,
    MatRadioModule,
    MatCheckboxModule,
    MatOptionModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
    MatTableModule,
    MatStepperModule,
    MatGridListModule,
    MatExpansionModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
