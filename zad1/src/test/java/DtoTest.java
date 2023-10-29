import domain.Movie;
import dto.Dto;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;
import java.util.List;

@DisplayName("Test DTO")
public class DtoTest {

    private Dto dto;
    private List<Movie> movieList;
    private Movie deerHunter;
    private Movie spalovacMrtvol;
    private Movie cabinetCaligari;

    @BeforeEach
    void setEnvironment() {
        this.deerHunter = new Movie("Lowca jeleni", LocalDate.of(1978, Month.DECEMBER, 8));
        this.spalovacMrtvol = new Movie("Palacz zwlok", LocalDate.of(1969, Month.MARCH, 14));
        this.cabinetCaligari = new Movie("Gabinet doktora Caligari", LocalDate.of(1920, Month.FEBRUARY, 26));

        this.movieList = new ArrayList<>();
        this.movieList.add(deerHunter);
        this.movieList.add(spalovacMrtvol);
        this.movieList.add(cabinetCaligari);

        this.dto = new Dto(this.movieList);
    }

    @Test
    void addMovie_When_AddNewMovieToDto_Expect_NewMovieInDto() {
        Movie newMovie = new Movie("Bravehart", LocalDate.of(1995, Month.MAY, 18));
        List<Movie> mockArray = new ArrayList<>();
        mockArray.add(this.deerHunter);
        mockArray.add(this.spalovacMrtvol);
        mockArray.add(this.cabinetCaligari);
        mockArray.add(newMovie);

        this.dto.addMovie(newMovie);

        assertArrayEquals(mockArray.toArray(), this.movieList.toArray());
    }

    @Test
    void getMovie_When_MovieInDto_Expect_Movie() {
        assertEquals(this.spalovacMrtvol, this.dto.getMovie(this.spalovacMrtvol));
    }

    @Test
    void getMovie_When_MovieNotInDto_Expect_Null() {
        Movie newMovie = new Movie("Bravehart", LocalDate.of(1995, Month.MAY, 18));
        Object returnObject = this.dto.getMovie(newMovie);
        assertNull(returnObject);
    }

    @Test
    void addMovie_When_MovieIsNull_Throws_NullPointerException() {
        Movie movie = null;
        assertThrows(NullPointerException.class, () -> this.dto.addMovie(movie));
    }

    @Test
    void removeMovie_When_MovieInDto_Expect_True() {
        assertTrue(this.dto.removeMovie(spalovacMrtvol));
    }

    @Test
    void removeMovie_When_MovieNotInDto_Expect_False() {
        Movie movieNotInDB = new Movie("cokolwiek", LocalDate.of(2000, Month.JANUARY, 1));
        assertFalse(this.dto.removeMovie(movieNotInDB));
    }

    @Test
    void getMovieList_Expect_WholeList() {
        List<Movie> mockArray = new ArrayList<>();
        mockArray.add(this.deerHunter);
        mockArray.add(this.spalovacMrtvol);
        mockArray.add(this.cabinetCaligari);

        assertArrayEquals(mockArray.toArray(), this.dto.getMovieList().toArray());
    }

    @Test
    void findMovie_When_MovieInDto_Expect_True() {
        assertTrue(this.dto.findMovie(this.spalovacMrtvol));
    }

    @Test
    void findMovie_When_MovieNotInDto_Expect_False() {
        Movie newMovie = new Movie("Bravehart", LocalDate.of(1995, Month.MAY, 18));
        assertFalse(this.dto.findMovie(newMovie));
    }

    @Test
    void removeMovie_When_RemoveAllMovies_Expect_EmptyList() {
        List<Movie> emptyList = new ArrayList<>();

        this.dto.removeMovie(this.spalovacMrtvol);
        this.dto.removeMovie(this.deerHunter);
        this.dto.removeMovie(this.cabinetCaligari);

        assertEquals(emptyList, this.dto.getMovieList());
    }
}
