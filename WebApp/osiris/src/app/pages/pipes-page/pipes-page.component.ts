import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {SelectionModel} from '@angular/cdk/collections';
import {MatTableDataSource} from '@angular/material/table';

export interface Pipe {
  name: string;
  source: string;
  model: string;
  state: string;
}

const ELEMENT_DATA: Pipe[] = [
  {name: 'CCTV-1', source: 'RTSP', model: 'YoloV3', state: 'true'},
  {name: 'In doors', source: 'USB', model: 'YoloV3', state: 'true'},
  {name: 'In door 2', source: 'USB', model: 'YoloV3', state: 'true'}
];

@Component({
  selector: 'app-pipes-page',
  templateUrl: './pipes-page.component.html',
  styleUrls: ['./pipes-page.component.css']
})
export class PipesPageComponent implements OnInit {
  displayedColumns: string[] = ['name', 'source', 'model', 'state'];
  dataSource = new MatTableDataSource<Pipe>(ELEMENT_DATA);
  selection = new SelectionModel<Pipe>(true, []);

  pipeline_states = ['Start', 'Stop', 'Terminate']

  constructor(private router: Router) { }

  /** Whether the number of selected elements matches the total number of rows. */
  isAllSelected() {
    const numSelected = this.selection.selected.length;
    const numRows = this.dataSource.data.length;
    return numSelected === numRows;
  }

  /** Selects all rows if they are not all selected; otherwise clear selection. */
  masterToggle() {
    this.isAllSelected() ?
        this.selection.clear() :
        this.dataSource.data.forEach(row => this.selection.select(row));
  }

  /** The label for the checkbox on the passed row */
  checkboxLabel(row?: Pipe): string {
    if (!row) {
      return `${this.isAllSelected() ? 'select' : 'deselect'} all`;
    }
    return `${this.selection.isSelected(row) ? 'deselect' : 'select'} row ${row.name}`;
  }

  ngOnInit() {
  }

  createNewPipeButtonClick() {
    this.router.navigateByUrl('/pipes/launch');
  }

}
