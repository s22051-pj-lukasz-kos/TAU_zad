package application;

import domain.Movie;
import dto.Dto;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        Movie deerHunter = new Movie("Lowca jeleni", LocalDate.of(1978, Month.DECEMBER, 8));
        Movie spalovacMrtvol = new Movie("Palacz zwlok", LocalDate.of(1969, Month.MARCH, 14));
        Movie cabinetCaligari = new Movie("Gabinet doktora Caligari", LocalDate.of(1920, Month.FEBRUARY, 26));

        List<Movie> movieList = new ArrayList<>();
        movieList.add(deerHunter);
        movieList.add(spalovacMrtvol);
        movieList.add(cabinetCaligari);

        Dto dto = new Dto(movieList);
    }
}
